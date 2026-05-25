buffer = "jU5t_a_sna_3lpm15g64e_u_4_m1r74d"

password = [''] * 32

# First loop reverse
for i in range(0, 8):
    password[i] = buffer[i]

# Second loop reverse
for i in range(8, 16):
    password[23 - i] = buffer[i]

# Third loop reverse
for i in range(16, 32, 2):
    password[46 - i] = buffer[i]

# Fourth loop reverse
for i in range(31, 16, -2):
    password[i] = buffer[i]

passwordstr = "".join(password)

print(passwordstr)
