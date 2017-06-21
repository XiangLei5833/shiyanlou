#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from faker import Factory
from sqlalchemy.orm import sessionmaker

faker = Factory.create()
Session = sessionmaker(bind=engine)
session = Aession()

faker_users = [User(
    username=faker.name(),
    password=faker.word(),
    email=faker.email(),)
    for i in range(10)]
sesson.add_all(faker_users)

faker_categories = [Category(name=faker.word()) for i in range(5)]
session.add_all(faker_categories)

faker_tags = [Tag(name=faker.word()) for i in range(20)]
session.add_all(faker_tags)

for i in range(100):
    article = Article(
        title=faker.sentence(),
        content=' '.join(faker.sentences(nb=random.randint(10, 20))),
        auther=random.choice(faker_users),
        category=random.choice(faker_categories))
    for tag in random.sample(faker_tags, random.randint(2,5)):
        article.tags.append(tag)
    session.add(article)

session.commit()

# Create teatdata use Faker
