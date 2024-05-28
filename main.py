import secrets
import sys


if __name__ == '__main__':
    if len(sys.argv) == 0:
        print('Usage: sct [OPTION]...')
        exit(1)
    
    args = sys.argv[1:]
    
    for i in range(0, len(args) - 1):
        arg = args[i]

        if arg[0] == '-':
            if arg[1:] == 'tokenbytes':
                print(secrets.token_bytes(int(args[i+1])))
                exit(0)
            elif arg[1:] == 'tokenhex':
                print(secrets.token_hex(int(args[i+1])))
                exit(0)
            elif arg[1:] == 'tokenurlsafe':
                print(secrets.token_urlsafe(int(args[i+1])))
                exit(0)
        else:
            print('Invalid syntax')
            exit(2)


    print(args)

