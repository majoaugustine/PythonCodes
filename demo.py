a='majo'
b='augustine'
print('my name is',a,b)
list1=[1,2,3,'slop']
print(list1)
list2=['helan','sunu','majo',('menon',2,4)]
print(list1+list2)
print(type(list2))
list3 = list((2,3,4,5))
print(type(list3))
d={'name':'majo',
   'place':'kannur'}
print(d)
f={
    'student':{
        'name': 'majo',
        'roll':'30',
        'sub':{
                '301':'ds',
                '302':'java'
        }
    }
}
print(f.get('student').get('sub'))
f['student']['sub']['301']='finance'
print(f.get('student').get('sub'))
l2=[5,6,7,8,]
l1=l2.copy()
print(l1)
set1={1,2,3,4,5}
set2={'a','b','c','d',21,21,23,24}
print(set1,set2)
