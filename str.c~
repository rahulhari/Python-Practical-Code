#include<stdio.h>
#include<string.h>
void  sub(char s1[20],char s2[20],int ,int ,int );
int main()
{
	char s1[20],s2[20],s;
	int l,i,p,g;
	printf("\n Enter the string:");
	gets(s1);
	l=strlen(s1);
	printf("\n Enter the sub-string:");
	gets(s2);
	printf("\n Enter the position of the sub-string:");
	scanf("%d",&p);
	g=strlen(s2);
	sub(s1[12],s2[29],p,l,g);
	return 0;
}
void sub(char s1[20],char s2[20],int p,int l,int g)
{
	int i,j;
	for(i=l;i<=p-1;i++)
	{
		s1[i+1]=s1[i];
	}
	for(i=p-1;i<g;i++)
	{
		if(i==p-1)
		{
		while(i!=g)
		{
			for(j=0;j<g;j++)
			{
				strcpy(s1[i],s2[j]);
				i++;
			}
		}
		}
		else
			break;
	}
	printf("The string is %s", s1);
}
