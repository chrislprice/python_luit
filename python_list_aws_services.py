#Define the empty list
my_aws_list=[]
print("List is empty: ", my_aws_list)

#Enter vlaues into the list using append
my_aws_list.append('RDS')
my_aws_list.append('S3')
my_aws_list.append('Lambda')

#Can also use "insert" to enter values into the list
my_aws_list.insert(3,'EC2')  


#Print the contents of the list
print("Contents of the list after entering values: ", my_aws_list)

#Print the length of the list
print("The lengh of the list: ", len(my_aws_list))


#Delete two values from the list
del my_aws_list[1:3]
print("The remaining contents of the list after deleting two values: ", my_aws_list)


print("New length of the list after the delete: ", len(my_aws_list))
