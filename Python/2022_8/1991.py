#실버1 트리 순회
import sys
input=sys.stdin.readline

n=int(input())
tree={}
result=[] #각 결과 첨가
for i in range(n):
    root, left, right=input().strip().split()
    tree[root]=[left,right]
def preorder(root):
    if root !='.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])
def midorder(root):
    if root !='.':
        midorder(tree[root][0])
        print(root, end='')
        midorder(tree[root][1])
def passorder(root):
    if root !='.':
        passorder(tree[root][0])
        passorder(tree[root][1])
        print(root, end='')
preorder('A')
print()
midorder('A')
print()
passorder('A')
