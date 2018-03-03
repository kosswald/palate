import boto3
s3 = boto3.resource('s3')
bucket= s3.Bucket('palate')

lst= open("palate.lst",'w')
def reverse(str):
    newstr = ""
    for i in xrange(len(str) - 1, -1, -1):
        newstr += str[i]
    return newstr


for bucket in s3.buckets.all():
    counter=0
    for key in bucket.objects.all():
        counter+= 1
        path= key.key.encode('utf-8')
        r_name = ""
        for i in xrange(len(path)-1, 0, -1):
            #print(path[i])
           #print(path[i])
           if path[i]=='/':
               i = i - 1
               while path[i]!='/':
                   r_name += path[i]
                   i = i - 1
               break
        lst.write(str(counter))
        lst.write("\t")
        lst.write(reverse(r_name))
        lst.write("\t")
        lst.write(path)
        lst.write("\n")

        #print(reverse(r_name))
        #print(key.key)
        #print(counter)

with open("palate.lst",'r') as fin:
    print fin.read()



