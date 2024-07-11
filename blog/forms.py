from django import forms
from .models import Post, Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    tags = forms.CharField(max_length=200, help_text='Enter tags separated by commas')

    def save(self, commit=True):
        post = super().save(commit=False)
        tag_names = self.cleaned_data['tags'].split(',')
        if commit:
            post.save()
            post.tags.set(*[Tag.objects.get_or_create(name=name.strip())[0] for name in tag_names])
        return post

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
