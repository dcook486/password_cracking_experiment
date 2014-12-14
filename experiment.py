import string
import random
from time import time


def make_password(num_characters, **kwargs):
    chars = []
    if "uppercase" in kwargs and kwargs["uppercase"]:
        chars.extend(string.ascii_uppercase)
    if "lowercase" in kwargs and kwargs["lowercase"]:
        chars.extend(string.ascii_lowercase)
    if "punctuation" in kwargs and kwargs["punctuation"]:
        chars.extend(string.punctuation)
    if ("digits" in kwargs and kwargs["digits"]) or len(chars) == 0:
        chars.extend(string.digits)
    return "".join([random.choice(chars) for i in range(num_characters)])


if __name__ == "__main__":
	secret_password = make_password(
        num_characters=2,
        uppercase=False,
        lowercase=False,
        punctuation=False,
        digits=True
    )


	# str(3) + str(4)
	# str(3) + str(4) == secret_password

	possible_chars = string.digits + string.ascii_lowercase

	if len(secret_password) == 2:
		tic = time()
		for i in possible_chars:
			for j in possible_chars:
				password_to_check = i + j
				if password_to_check == secret_password:
					toc = time()
					# print "Great Success!!"
					# print "It took", toc - tic, "seconds"
					# print "To crack the password", password_to_check
					print toc - tic
					exit()

	elif len(secret_password) == 4:
		# David's code goes here
		tic = time()
		for i in possible_chars:
			for j in possible_chars:
				for k in possible_chars:
					for l in possible_chars:
						password_to_check = i + j + k + l
						if password_to_check == secret_password:
							toc = time()
							print "Great Success!!"
							print "It took", toc - tic, "seconds"
							print "To crack the password", password_to_check
							exit()

	elif len(secret_password) == 8:
		# Here's some more of David's code
		tic = time()
		for i in possible_chars:
			for j in possible_chars:
				for k in possible_chars:
					for l in possible_chars:
						for m in possible_chars:
							for n in possible_chars:
								for o in possible_chars:
									for p in possible_chars:
										password_to_check = i + j + k + l + m + n + o + p
										print password_to_check
										if password_to_check == secret_password:
											toc = time()
											print "Great Success!!"
											print "It took", toc - tic, "seconds"
											print "To crack the password", password_to_check
											exit()

	else:
		print "This password is UNCRACKABLE!!!!"

