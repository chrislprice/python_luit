#script creates and empty list
#Enter values into the list, print the contents of the list, and length of the list
#Delete two values from the list
#Print the remaining contents and new lenth of the list after the delete statement

#Define the empty list
my_aws_list=[]
print("List is empty: ", my_aws_list)

#Enter values into the list using append
my_aws_list.append('RDS')
my_aws_list.append('S3')
my_aws_list.append('Lambda')

#Can also use "insert" to enter values into the list
my_aws_list.insert(3,'EC2')  


#Print the contents of the list
print("Contents of the list after entering values: ", my_aws_list)

#Print the length of the list
print("The length of the list: ", len(my_aws_list))


#Delete two values from the list
del my_aws_list[1:3]
print("Contents of the list after deleting two values: ", my_aws_list)

#Print the new length after the delete statement
print("Length of the list after the delete: ", len(my_aws_list))
