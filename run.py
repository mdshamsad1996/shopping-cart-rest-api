"""
Run Module 
"""
from src import app

if __name__ == '__main__':
    """
    run app using run method
    """
    app.run(debug=True, host='0.0.0.0')