from matplotlib import pyplot as plt

# my_data = [71, 53.3, 83]
# my_labels = ['Tasks Pending', 'Tasks Ongoing', 'Tasks Completed']
#
#
# plt.pie(my_data, labels=my_labels, autopct='%1.1f%%')
# plt.title('My Tasks')
# plt.axis('equal')
# plt.show()
# country = ['A', 'B', 'C', 'D', 'E']
# gdp_per_capita = [45000, 42000, 52000, 49000, 47000]
#
# plt.bar(country, gdp_per_capita)
# plt.title('Country Vs GDP Per Capita')
# plt.xlabel('Country')
# plt.ylabel('GDP Per Capita')
# plt.show()

test_cases_data = ["Test Case One", "Test Case Two", "Test Case 33"]
status = [76.3, 55, 1]
plt.bar(test_cases_data,status,height=100)
plt.xlabel("Test Case information")
plt.ylabel("Pass percentage")
plt.show()
