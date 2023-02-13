
#################################
# Function for finding the roots 
# of a quadratic polynomial 
#################################

# This function takes as inputs the coefficients a,b,c
# of a polynomial P(x)=a*x^2+b*x+c and returns its real 
# roots or NULL if there are no real roots. 


quadroot = function(a,b,c)
{

	# Case: polynomial of degree d<2 
	if (a == 0)
	{
		# Case: constant polynomial (d=0)
		if (b == 0)
		{ 
			# Case: null function 
			if (c == 0) 
			{
				stop("null function: all real numbers are roots")
			} else { # Case: constant, nonzero function (--> no roots)
				return(NULL)	
			}	
		}
		# Case: linear polynomial (d=1)
		return(-c/b)
	} 
	
	# Regular case: degree d=2
	# Discriminant
	delta = b^2 - 4*a*c
	if (delta > 0)
	{
		r1 = (-b-sqrt(delta))/(2*a)
		r2 = (-b+sqrt(delta))/(2*a)
		return(c(r1,r2)) 
	} else if (delta == 0)
	{
		r1 = -b/(2*a)
		return(r1)
	} else {
		return(NULL)
	}	
	
}

