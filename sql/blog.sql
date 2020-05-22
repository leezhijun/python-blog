--创建数据库
CREATE DATABASE IF NOT EXISTS `blog`;
--使用表
use `blog`;

--主表/基本站点信息
CREATE TABLE IF NOT EXISTS `blog_site`(
   `site_id` INT(10) UNSIGNED AUTO_INCREMENT COMMENT '自增id',
   `site_key` VARCHAR(255) NOT NULL UNIQUE COMMENT '键',
   `site_name` VARCHAR(255) NOT NULL COMMENT '名称',
   `site_value` TEXT COMMENT '值',
   PRIMARY KEY ( `site_id` ),
   KEY `sitekey` (`site_key`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `blog_site` (`site_key`, `site_name`) VALUES ('site_name','站点名称');
INSERT INTO `blog_site` (`site_key`, `site_name`) VALUES ('site_url','网址');
INSERT INTO `blog_site` (`site_key`, `site_name`) VALUES ('site_title','网站标题');
INSERT INTO `blog_site` (`site_key`, `site_name`) VALUES ('site_keywords','关键词');
INSERT INTO `blog_site` (`site_key`, `site_name`) VALUES ('site_descript','描述');
INSERT INTO `blog_site` (`site_key`, `site_name`) VALUES ('site_email','站点邮箱');
INSERT INTO `blog_site` (`site_key`, `site_name`) VALUES ('site_copy','备案信息');
INSERT INTO `blog_site` (`site_key`, `site_name`) VALUES ('site_views_count','访问人数');

--用户表
CREATE TABLE IF NOT EXISTS `blog_user`(
   `user_id` BIGINT(20) UNSIGNED AUTO_INCREMENT COMMENT '自增id',
   `user_name` VARCHAR(50) NOT NULL UNIQUE COMMENT '用户名',
   `user_password` CHAR(32) NOT NULL COMMENT '密码',
   `user_email` VARCHAR(255) UNIQUE COMMENT '邮箱',
   `user_phone` CHAR(11) UNIQUE COMMENT '手机',
   `user_level` TINYINT(2) NOT NULL DEFAULT 0 COMMENT '用户等级',
   `user_img` VARCHAR(255) COMMENT 'logo',
   `user_registered_time` DATETIME NOT NULL COMMENT '注册时间',
   `user_birthday` DATE COMMENT '出生日',
   `user_last_login_time` DATETIME NOT NULL COMMENT '最后登陆时间',
   `user_ip` VARCHAR(100) COMMENT '登陆ip',
   `user_activation_key` CHAR(32) COMMENT '激活码',
   `user_status` TINYINT(2) NOT NULL DEFAULT 0 COMMENT '用户状态(1激活 0未激活 2小黑屋)',
   PRIMARY KEY ( `user_id` ),
   KEY `username` (`user_name`),
   KEY `useremail` (`user_email`),
   KEY `userphone` (`user_phone`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--默认用户名 admin 密码 123456
INSERT INTO `blog_user` (`user_name`, `user_password`,`user_level`,`user_registered_time`,`user_last_login_time`,`user_status`) 
VALUES ('admin','8cef992a5af6b216dd3c62ae39f4a13b',99,NOW(),NOW(),1);

--类目表
CREATE TABLE IF NOT EXISTS `blog_cate`(
   `cate_id` SMALLINT(4) UNSIGNED AUTO_INCREMENT COMMENT '自增id',
   `cate_name` VARCHAR(50) NOT NULL UNIQUE COMMENT '类目名',
   `cate_title` VARCHAR(200) COMMENT '标题',
   `cate_keywords` VARCHAR(255) COMMENT '关键词',
   `cate_description` VARCHAR(500) COMMENT '描述',
   `cate_img` VARCHAR(255) COMMENT '类目img',
   `cate_order` TINYINT(3) UNSIGNED NOT NULL DEFAULT 10 COMMENT '类目排序',
   `cate_show` TINYINT(2) UNSIGNED NOT NULL DEFAULT 1 COMMENT '是否展示-1展示',
   `cate_parent_id` TINYINT(4) UNSIGNED NOT NULL COMMENT '父级id',
   `cate_icon` VARCHAR(32) COMMENT '图标',
   PRIMARY KEY ( `cate_id` ),
   KEY `catename` (`cate_name`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--文章表
CREATE TABLE IF NOT EXISTS `blog_article`(
   `article_id` BIGINT(20) UNSIGNED AUTO_INCREMENT COMMENT '自增id',
   `user_id` BIGINT(20) NOT NULL COMMENT '用户id',
   `cate_id` SMALLINT(4) COMMENT '分类id',
   `article_title` VARCHAR(200) NOT NULL COMMENT '标题',
   `article_keywords` VARCHAR(255) COMMENT '关键词',
   `article_description` VARCHAR(500) COMMENT '描述',
   `article_is_hot` TINYINT(2) UNSIGNED NOT NULL DEFAULT 0 COMMENT '热门 1是 0否',
   `article_is_push` TINYINT(2) UNSIGNED NOT NULL DEFAULT 0 COMMENT '推荐 1是 0否',
   `article_img` VARCHAR(255) COMMENT '文章img',
   `article_content` LONGTEXT NOT NULL COMMENT '文章内容',
   `article_publish_time` DATETIME NOT NULL COMMENT '发布时间',
   `article_update_time` DATETIME NOT NULL COMMENT '最后修改时间',
   `article_browse_count` BIGINT(20) UNSIGNED NOT NULL DEFAULT 0 COMMENT '浏览次数',
   `article_like_count` BIGINT(20) UNSIGNED NOT NULL DEFAULT 0 COMMENT '点赞次数',
   `article_status` TINYINT(2) UNSIGNED NOT NULL DEFAULT 1 COMMENT '状态(1发布0草稿2待审核3回收站)',
   `article_comment_status` TINYINT(2) UNSIGNED NOT NULL DEFAULT 0 COMMENT '是否评论1是0否',
   `article_password` CHAR(32) COMMENT '文章密码',
   `article_order` TINYINT(2) UNSIGNED NOT NULL DEFAULT 10 COMMENT '文章排序',
   `article_type` TINYINT(2) UNSIGNED NOT NULL DEFAULT 1 COMMENT '类型1文章2单页',
   PRIMARY KEY ( `article_id` ),
   KEY `userid` (`user_id`),
   KEY `cateid` (`cate_id`),
   KEY `articletitle` (`article_title`),
   KEY `articleupdatetime` (`article_update_time`),
   KEY `articleorder` (`article_order`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--评论表
CREATE TABLE IF NOT EXISTS `blog_comment`(
   `comment_id` BIGINT(20) UNSIGNED AUTO_INCREMENT COMMENT '自增id',
   `article_id` BIGINT(20) NOT NULL COMMENT '文章id',
   `user_id` BIGINT(20) COMMENT '用户id',
   `comment_content` TEXT COMMENT '评论内容',
   `comment_date` DATETIME COMMENT '评论时间',
   `comment_status` TINYINT(2) NOT NULL DEFAULT 0 COMMENT '状态0审核1发布2回收',
   `comment_parent` BIGINT(20) NOT NULL COMMENT '评论父级id',
   PRIMARY KEY ( `comment_id` ),
   KEY `articleid` (`article_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--友情连接
CREATE TABLE IF NOT EXISTS `blog_link`(
   `link_id` TINYINT(3) UNSIGNED AUTO_INCREMENT COMMENT '自增id',
   `link_name` VARCHAR(50) NOT NULL COMMENT '名称',
   `link_url` VARCHAR(255) NOT NULL COMMENT '链接地址',
   `link_status` TINYINT(3) UNSIGNED NOT NULL DEFAULT 0 COMMENT '状态0未启用1启用',
   PRIMARY KEY ( `link_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--标签表
CREATE TABLE IF NOT EXISTS `blog_tag`(
   `tag_id` BIGINT(20) UNSIGNED AUTO_INCREMENT COMMENT '自增id',
   `tag_name` VARCHAR(50) NOT NULL COMMENT '标签名',
   -- `tag_alias` VARCHAR(80) NOT NULL COMMENT '标签别名',
   `tag_order` TINYINT(2) UNSIGNED NOT NULL DEFAULT 10 COMMENT 'tag排序',
   `tag_img` VARCHAR(255) COMMENT '标签img',
   `tag_description` VARCHAR(500) COMMENT '标签描述',
   PRIMARY KEY ( `tag_id` ),
   KEY `tagorder` (`tag_order`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--标签/文章关联表
CREATE TABLE IF NOT EXISTS `blog_tag_and_article`(
   `tag_id` BIGINT(20) NOT NULL COMMENT '标签id',
   `article_id` BIGINT(20) NOT NULL COMMENT '文章id',
   KEY `articleid` (`article_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--用户/文章关联表-收藏
CREATE TABLE IF NOT EXISTS `blog_user_and_article`(
   `user_id` BIGINT(20) NOT NULL COMMENT '用户id',
   `article_id` BIGINT(20) NOT NULL COMMENT '文章id',
   KEY `userid` (`user_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--用户/文章关联表-收藏
CREATE TABLE IF NOT EXISTS `blog_img-list`(
   `article_id` BIGINT(20) NOT NULL COMMENT '文章id',
   `img_url` VARCHAR(255) NOT NULL COMMENT '图片路径',
   KEY `articleid` (`article_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;