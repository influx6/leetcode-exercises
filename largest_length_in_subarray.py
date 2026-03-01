# Uses sliding window and binary search to find the larget possible
# sub array and length possible for a average of the sum of the sub array that
# is roughly averga that is atleast X, so >= X.
#
# If we do: AVG = (SumOfSubArray / LengthOfSubArray) >= X
#
# Then we can re-express this as:
#
# First Reformulation: AVG = (SumOfSubArray / LengthOfSubArray) * LengthOfSubArray>= X * LengthOfSubArray
# Second Reformulation: AVG = SumOfSubArray >= X * LengthOfSubArray
# Third Reformulation: AVG = (SumOfSubArray - X * LengthOfSubArray) >= (X * LengthOfSubArray ) - (X * LengthOfSubArray)
# We know: (X * LengthOfSubArray) - (X * LengthOfSubArray) = 0 (since both values subtract each other)
#
# Final Reformulation: AVG = SumOfSubArray - (X * LengthOfSubArray) >= 0
#
