from django.shortcuts import render

posts = [
		{
		'author':'Kaustubh Bhatt',
		'title':'Blog Post 1',
		'content':'First post content',
		'date_posted':'20 september 2020'

		},
		{
		'author':'Christiano Ronaldo',
		'title':'Blog Post 2',
		'content':'Second post content',
		'date_posted':'21 september 2020'
		}
]

def home(request):
	context = {'posts': posts}
	return render(request,'blog/home.html', context) #the second arguement refers to the subdirectory in the templates directory
	

def about(request):
	return render(request,'blog/about.html', {'title': 'About'})	
