from flask import Flask, request, jsonify
from flask_cors import CORS
from game import get_slot_machine_spin, check_winnings, symbol_count, ROWS, COLS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Requests

@app.route('/spin', methods=['POST'])
def spin():
    data = request.json
    bet = int(data['bet'])
    lines = int(data['lines'])

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_count)

    return jsonify({
        'slots': slots,
        'winnings': winnings,
        'winning_lines': winning_lines
    })

if __name__ == '__main__':
    app.run(debug=True)
