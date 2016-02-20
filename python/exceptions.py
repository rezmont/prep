def main():
	print 'here'
	try:
		a = 10/0
	except Exception, e:
		print e
		print Exception
		raise
	else:
		pass
	finally:
		pass

if __name__ == '__main__':
	main()