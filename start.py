from App import app

def test_1():
    asssert(1==1)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
