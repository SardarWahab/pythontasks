# para = "Wahab"
# print(para.split('Wahab'))
# print(para.endswith('b'))
# print(para.startswith('W'))


para = """To improve communication within our team, please reach out to the following individuals for specific inquiries: For project updates, contact Emily at emily.project@company.com; for financial matters, email Mark at mark.finance@company.com; if you need IT support, get in touch with Sarah at sarah.tech@company.com; for HR-related questions, email Hannah at hannah.hr@company.com; and for any general inquiries, you can reach out to John at john.info@company.com."""

para_list = para.split(" ")
li = []
# print(para_list)
for x in para_list:
     if '.com' in x:
        print(x)  # prints the email addresses  
        li.append(x)
print(li)  
print(len(li))
 
