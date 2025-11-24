"""
Flask API for Package Sorting System
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from package_sorter import sort

app = Flask(__name__, static_folder='.')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/sort', methods=['POST'])
def sort_package():
    """API endpoint to sort a package."""
    try:
        data = request.json
        
        # Extract and validate inputs
        width = float(data.get('width', 0))
        height = float(data.get('height', 0))
        length = float(data.get('length', 0))
        mass = float(data.get('mass', 0))
        
        # Sort the package
        result = sort(width, height, length, mass)
        
        # Calculate volume and determine flags
        volume = width * height * length
        isBulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
        isHeavy = mass >= 20
        
        return jsonify({
            'success': True,
            'result': result,
            'details': {
                'volume': volume,
                'is_bulky': isBulky,
                'is_heavy': isHeavy,
                'bulky_reason': get_bulky_reason(width, height, length, volume) if isBulky else None
            }
        })
    
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An error occurred processing your request'
        }), 500

def get_bulky_reason(width, height, length, volume):
    """Determine why a package is bulky."""
    reasons = []
    if volume >= 1_000_000:
        reasons.append(f'Volume: {volume:,.0f} cm³ ≥ 1,000,000 cm³')
    if width >= 150:
        reasons.append(f'Width: {width} cm ≥ 150 cm')
    if height >= 150:
        reasons.append(f'Height: {height} cm ≥ 150 cm')
    if length >= 150:
        reasons.append(f'Length: {length} cm ≥ 150 cm')
    return ' | '.join(reasons)

if __name__ == '__main__':
    app.run(debug=True, port=5000)