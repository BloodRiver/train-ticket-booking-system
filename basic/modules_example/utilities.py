def check_email_validity(email):
    is_valid = True

    # example valid emails:
    # a@b.com
    # a@b.c
    # a.b@c.d
    # sajeed@gmail.com
    # sajeed@g.mailcom
    # sajeed@g.mail.com
    # saje.ed@g.mail.com
    
    # example invalid emails:
    # sajeed@gmailcom
    # @a
    # .a
    # a@
    # a.
    # a@b@c.d

    # 1. email can not start with @ symbol (done)
    if email[0] == "@":
        is_valid = False

    # 2. email can not start with . symbol (done)
    if email[0] == ".":
        is_valid = False

    # 6. email must NOT end with . symbol (done)
    if email[len(email) - 1] == "@":
        is_valid = False

    # 7. email must NOT end with @ symbol (done)
    if email[len(email) - 1] == ".":
        is_valid = False

    # 3. email must have exactly 1 @ symbol
    # so we will count how many @ symbols are there
    at_symbol_count = 0
    char_after_at_count = 0
    dot_after_char_after_at_count = 0
    
    # at_symbol_count = 0 + 1 = 1
    # char_after_at_count = 0 + 1 = 1
    # 0 1 2 3 4 5 6 7
    # a ! @ b @ c . d
    #     i

    rejected_characters = ["!", "#", "$", "%", "^", "&", "*", "(", ")", "+", "=", "-", "_"]

    for i in range(len(email)):
        # 8. email must NOT contain any special character such as 
        if email[i] in rejected_characters:
            is_valid = False
            break

        if email[i] == "@":
            at_symbol_count += 1
        else:
            if email[i] == ".":
                # 5. email must have at least 1 . symbol after the character(s) after the @ symbol
                if char_after_at_count > 0:
                    dot_after_char_after_at_count += 1
            else:
                # 4. email must have at least 1 character after the @ symbol
                if at_symbol_count == 1:
                    char_after_at_count += 1


    if at_symbol_count > 1:
        is_valid = False

    if char_after_at_count < 1:
        is_valid = False

    if dot_after_char_after_at_count < 1:
        is_valid = False

    return is_valid