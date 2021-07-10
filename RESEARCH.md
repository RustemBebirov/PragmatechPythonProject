# Template tags və filter
Template tag nədir?




Template filterler
{{blog.blog_author | upper }}
{{blog.blog_author | lover }}
{{comment.content | slice :'2'}}
{{comment.content | truncatechar:3}}
{{comment.content | truncatewords:4}}
{{blog.created_at | date:'F m' }}
{{blog.content | cut:' ' }}



