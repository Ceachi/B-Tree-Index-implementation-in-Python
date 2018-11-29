from Main import Main
import sys

def main():
    program = Main(int(sys.argv[1]), int(sys.argv[2]))
    program.run()

if __name__ == '__main__':
    main()  # Raises error on invalid flags, unlike tf.app.run()
