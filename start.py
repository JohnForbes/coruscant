from f.main import f as main
x = [
  {
    'plants': {
      'fruits': {'banana': 'yum', 'cherry': 2, 'durian': 3},
      'vegetables': {'eggplant': 1, 'fennel': 2, 'ginger': 3}
    }
  },
  {
    'plants': {
      'fruits': {'banana': 'delicious', 'cherry': 5, 'durian': 6},
      'vegetables': {'eggplant': 4, 'fennel': 5, 'ginger': 6}
    }
  },
]
y = """
                         plants                         
--------------------------------------------------------
          fruits            |         vegetables        
--------------------------- | --------------------------
 banana   | cherry | durian | eggplant | fennel | ginger
--------- | ------ | ------ | -------- | ------ | ------
   str    |  int   |  int   |   int    |  int   |  int  
--------- | ------ | ------ | -------- | ------ | ------
   yum    |   2    |   3    |    1     |   2    |   3   
delicious |   5    |   6    |    4     |   5    |   6   
"""

print(main(x))
