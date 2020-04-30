import sqlalchemy as sa

metadata = sa.MetaData()

blog_site = sa.Table('blog_site', metadata,
    sa.Column('site_id', sa.Integer, primary_key=True),
    sa.Column('site_key', sa.String(255), nullable=False),
    sa.Column('site_name', sa.String(255), nullable=False),
    sa.Column('site_value', sa.Text,  nullable=False),
)

blog_user = sa.Table('blog_user', metadata,
    sa.Column('user_id', sa.BigInteger, primary_key=True),
    sa.Column('user_name', sa.String(50), nullable=False),
    sa.Column('user_password', sa.String(32), nullable=False),
    sa.Column('user_email', sa.String(255)),
    sa.Column('user_phone', sa.String(11)),
    sa.Column('user_level', sa.SmallInteger, nullable=False),
    sa.Column('user_img', sa.String(255)),
    sa.Column('user_registered_time', nullable=False),
    sa.Column('user_birthday'),
    sa.Column('user_last_login_time', nullable=False),
    sa.Column('user_ip', sa.String(100)),
    sa.Column('user_activation_key', sa.String(32)),
    sa.Column('user_status', sa.SmallInteger, default=0),    
)

blog_cate = sa.Table('blog_cate', metadata,
    sa.Column('cate_id', sa.SmallInteger, primary_key=True),
    sa.Column('cate_name', sa.String(50), nullable=False),
    sa.Column('cate_title', sa.String(200)),
    sa.Column('cate_keywords', sa.String(255)),
    sa.Column('cate_description', sa.String(500)),
    sa.Column('cate_img', sa.String(255)),
    sa.Column('cate_order', sa.SmallInteger, nullable=False, default=10),
    sa.Column('cate_show', sa.SmallInteger, nullable=False, default=1),
    sa.Column('cate_parent_id', sa.SmallInteger, nullable=False),
)

blog_article = sa.Table('blog_article', metadata,
    sa.Column('article_id', sa.BigInteger, primary_key=True),
    sa.Column('user_id', sa.BigInteger, nullable=False),
    sa.Column('cate_id', sa.SmallInteger),
    sa.Column('article_title', sa.String(200), nullable=False),
    sa.Column('article_keywords', sa.String(255)),
    sa.Column('article_description', sa.String(500)),
    sa.Column('article_is_hot', sa.SmallInteger, nullable=False, default=0),
    sa.Column('article_is_push', sa.SmallInteger, nullable=False, default=0),
    sa.Column('article_img', sa.String(255)),
    sa.Column('article_content', sa.Text, nullable=False),
    sa.Column('article_publish_time', nullable=False),
    sa.Column('article_update_time', nullable=False),
    sa.Column('article_browse_count', sa.BigInteger, nullable=False, default=0),
    sa.Column('article_like_count', sa.BigInteger, nullable=False, default=0),
    sa.Column('article_status', sa.SmallInteger, nullable=False, default=1),
    sa.Column('article_comment_status', sa.SmallInteger, nullable=False, default=0),
    sa.Column('article_password', sa.String(32)),
    sa.Column('article_order', sa.SmallInteger, nullable=False, default=10),
    sa.Column('article_type', sa.SmallInteger, nullable=False, default=1),    
)

# blog_comment = sa.Table('blog_comment', metadata,
#     sa.Column('comment_id', sa.BigInteger, primary_key=True),
#     sa.Column('article_id', sa.BigInteger, nullable=False),
#     sa.Column('user_id', sa.BigInteger),
#     sa.Column('comment_content', sa.Text, nullable=False),
#     sa.Column('comment_date', sa.Time),
#     sa.Column('comment_status', sa.SmallInteger, nullable=False, default=0),
#     sa.Column('comment_parent', sa.BigInteger, nullable=False), 
# )

# blog_link = sa.Table('blog_link', metadata,
#     sa.Column('link_id', sa.SmallInteger, primary_key=True),
#     sa.Column('link_name', sa.String(50), nullable=False),
#     sa.Column('link_url', sa.String(255), nullable=False, default=0),
#     sa.Column('link_status', sa.SmallInteger, nullable=False),
# )

blog_tag = sa.Table('blog_tag', metadata,
    sa.Column('tag_id', sa.BigInteger, primary_key=True),
    sa.Column('tag_name', sa.String(50), nullable=False),
    sa.Column('tag_alias', sa.String(80), nullable=False),
    sa.Column('tag_order', sa.SmallInteger, nullable=False, default=0),
    sa.Column('tag_img', sa.String(255)),
    sa.Column('tag_description', sa.String(500)),
)

# blog_tag_and_article = sa.Table('blog_tag_and_article', metadata,
#     sa.Column('tag_id', sa.BigInteger, ullable=False),
#     sa.Column('article_id', sa.BigInteger, nullable=False),
# )

# blog_img = sa.Table('blog_img', metadata,
#     sa.Column('article_id', sa.BigInteger, nullable=False),
#     sa.Column('img_url', sa.String(255), nullable=False),
# )