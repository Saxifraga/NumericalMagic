import numpy 

def intpi(n):
	sums = 0 #this will be used to sum the functions from i=0 to n-1
	delta_x = n**(-1)
	for i in range(1,n):
		x_i = delta_x*i
		f_x_i = 4*(1-x_i**2)**0.5
		sums += f_x_i
	r_sum = delta_x*sums
	pi_est = r_sum
	true_error = abs(numpy.pi - pi_est)
	true_relative_error = true_error/numpy.pi
	true_relative_percent_error = true_relative_error*100
	print "n =", n
	print "delta_x =", delta_x
	print "pi estimate =", pi_est
	print "true error =", true_error
	print "true relative error =", true_relative_percent_error, "%"
	return pi_est

n_list = [10,50,100,500,1000,5000]
for n in n_list: 
	current_approx = intpi(n)
	if n > 10: 
		approximate_relative_error = abs(100*(current_approx-prev_approx)/current_approx)
		print "approximate relative error =", approximate_relative_error, "%"
	print ''
	prev_approx = current_approx






