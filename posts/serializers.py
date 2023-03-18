from rest_framework import serializers
from html.parser import HTMLParser
from .models import Post


class HTMLFilter(HTMLParser):
    text = ""
    def handle_data(self, data):
        self.text += data


class PostSerializer(serializers.ModelSerializer):
    featured_content = serializers.SerializerMethodField('get_featured_content')
    short_content = serializers.SerializerMethodField('get_short_content')

    def get_cut_content(self, content: str, paragraph_length: int, char_length: int):
        paragraph_list = content.split('</p>')[0:paragraph_length]
        html_text = '</p>'.join(paragraph_list) + '</p>'
        html_filter = HTMLFilter()
        html_filter.feed(html_text)
        cut_content = html_filter.text[0:char_length]
        word_list = cut_content.strip().split()
        suffix = ''
        if len(cut_content) == char_length:
            word_list.pop()
            suffix = '...'
        return ' '.join(word_list) + suffix

    def get_featured_content(self, post):
        return self.get_cut_content(content=post.content, paragraph_length=2, char_length=500)

    def get_short_content(self, post):
        return self.get_cut_content(content=post.content, paragraph_length=1, char_length=200)

    class Meta:
        model = Post
        fields = ('post_id', 'create_date', 'author', 'title', 'content', 'featured_content', 'short_content',
                  'birth_date', 'death_date', 'is_public')
        read_only_fields = ('post_id', 'create_date', 'featured_content', 'short_content')
