### Normal Distribution
Normal Distribution is a continuous probability distribution. It is also called Gaussian distribution.
It is a bell-shaped curve. It is defined by its center (mean) and spread (standard deviation).
The probability density function of the normal distribution is:
f(x|μ,σ^2) = (1/√(2πσ^2)) * e^(-((x-μ)^2)/(2σ^2)) where x is the value of the variable, μ is the mean, σ is the standard deviation, π is the constant pi, and e is the constant e.
The standard normal distribution is a normal distribution with a mean of 0 and standard deviation of 1.
The standard normal distribution is denoted by N(0,1).
The cumulative distribution function of the standard normal distribution is denoted by Φ(z).
Φ(z) = (1/√(2π)) * ∫(from -∞ to z) e^(-t^2/2) dt where z is the value of the standard normal variable, π is the constant pi, e is the constant e, and Φ is the cumulative distribution function of the standard normal distribution.
The cumulative distribution function of the normal distribution is:
Φ(x|μ,σ^2) = Φ((x-μ)/σ) where x is the value of the variable, μ is the mean, σ is the standard deviation, and Φ is the cumulative distribution function of the standard normal distribution.   
The cumulative distribution function gives the probability that the variable takes a value less than or equal to x.
The cumulative distribution function is also called the normal probability function.
The cumulative distribution function of the standard normal distribution is also called the error function.
The cumulative distribution function of the standard normal distribution is denoted by erf(z).
erf(z) = (2/√π) * ∫(from 0 to z) e^(-t^2) dt where z is the value of the standard normal variable, π is the constant pi, e is the constant e, and erf is the cumulative distribution function of the standard normal distribution.
The cumulative distribution function of the normal distribution is:
Φ(x|μ,σ^2) = (1/2) * (1 + erf((x-μ)/(σ√2))) where x is the value of the variable, μ is the mean, σ is the standard deviation, π is the constant pi, e is the constant e, and erf is the cumulative distribution function of the standard normal distribution. -->

#### Example 1
Let's say the average height of a 
population is 5.6 feet and the standard deviation is 2.8 feet.
What is the probability that a person chosen at random is less than 6 feet tall?
We need to find the probability that a person is less than 6 feet tall.
We can use the cumulative distribution function of the normal distribution.
Φ(x|μ,σ^2) = Φ((x-μ)/σ)
Φ(6|5.6,2.8^2) = Φ((6-5.6)/2.8)
Φ(6|5.6,2.8^2) = Φ(0.14285714285714285)
Φ(6|5.6,2.8^2) = 0.556371
The probability that a person chosen at random is less than 6 feet tall is 0.556371.