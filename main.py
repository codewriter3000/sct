import secrets
import sys

def main():
    if len(sys.argv) == 1:
        print('Usage: sct [OPTION]...')
        exit(1)
   
    args = sys.argv[1:]

    for i in range(0, len(args) - 1):
        arg = args[i]
        
        if arg[0:2] == '--':
            if arg[2:] == 'tokenbytes':
                token_bytes(args[i+1])
            elif arg[2:] == 'tokenhex':
                token_hex(args[i+1])
            elif arg[2:] == 'tokenurlsafe':
                token_urlsafe(args[i+1])
        else:
            print('Invalid syntax')
            exit(2)


def token_bytes(size):
    print(secrets.token_bytes(int(size)))


def token_hex(size):
    print(secrets.token_hex(int(size)))


def token_urlsafe(size):
    print(secrets.token_urlsafe(int(size)))


if __name__ == '__main__':
   main()

