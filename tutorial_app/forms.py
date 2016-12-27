from django import forms
from models import Page, Category, UserProfile
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.utils.crypto import get_random_string

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput()) #So that the password is hidden

	class Meta: 
		model = User #this means create a new user using the following
		fields = ('username', 'password', 'email')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website', 'picture', 'bio')

class CategoryForm(forms.ModelForm): #this created a new form for us
	name = forms.CharField(max_length=128, help_text='Please enter a category name!')
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0) #creates a field but doesnt let the user see it 
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	
	class Meta: #this tells the form what model to associate it with and what type of model to create
		model = Category
		fields = ('name',) #specify that you are not showing all the fields
		exclude = ('user',)

class PageForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text='Please enter a page title')
	url = forms.URLField(max_length=200, help_text='Please enter page URL!')
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url') #get the url from the form

		if url and not url.startswith('http://'):
			url = 'http://'+ url
			cleaned_data['url'] = url
		return cleaned_data 

	class Meta:
		model = Page
		exclude = ('category', 'user')

class ContactForm(forms.Form):
	name = forms.CharField(required=True)
	email = forms.CharField(widget=forms.EmailInput(), required=True)
	subject = forms.CharField(required=True)
	body = forms.CharField(widget=forms.Textarea(), required=True)

	def send_message(self):
		name = self.cleaned_data['name']
		email = self.cleaned_data['email']
		subject = self.cleaned_data['subject']
		body = self.cleaned_data['body']

		message = '''
				New Message from {name} @ 
				{email}
				Subject: {subject}
				Message:
				{body}
				'''.format(name=name, email=email, subject=subject, body=body)

		email_msg = EmailMessage('New Contact Form Submission',
					message,
					email,
					['jenpaulino3@gmail.com'])

		email_msg.send()

class PasswordRecoveryForm(forms.Form):
	email = forms.EmailField(required=False)

	def clean_email(self):
		try:
			return User.objects.get(email=self.cleaned_data['email'])
		except User.DoesNotExist:
			raise forms.ValidationError("Can't find a user based on this email")
		return self.cleaned_data('email')
	
	def reset_password(self):
		
		user = self.cleaned_data['email']

		password = get_random_string(length=8)

		user.set_password(password)

		user.save()

		body = """
				Sorry you are having issues with your account! Below is your user name and new password

				Username: {username}
				Password: {password}

				You can log in here: http://localhost:8000/login/
				You can change your password here: http://localhost:8000/settings/

				""".format(username=user.username, password=password)

		pw_msg = EmailMessage('Your new password', body, 'jenpaulino3@gmail.com', [user.email])

		pw_msg.send()
