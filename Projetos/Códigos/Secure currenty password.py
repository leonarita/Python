SECURE = (('s', '$'), ('and', '&'), ('o', '0'), ('i', '!'))


def securePassword(password):
    for a, b in SECURE:
        password = password.replace(a, b)

    return password


if __name__ == '__main__':
    password = input('Enter your password: ')
    print(f"Your new secure password: {securePassword(password.lower())} ")
