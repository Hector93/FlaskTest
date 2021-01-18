from app import appInstance
from seed import main
import sys
# start of the flask project, by default the database is populated with 150 elements
# but you can pass the number of elements to retrive as a paramenter
# example python server 10
if __name__ == '__main__':
    args = sys.argv
    total = 150
    if len(args) == 2:
        total = int(args[1])
    print(total)
    main(total)
    appInstance.run(debug=False)
