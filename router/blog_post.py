from typing import Dict, List, Optional
from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    nb_comments: int
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1': 'val1'}
    image: Optional[Image] = None

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog,
        'version': version
        }

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel, id: int,
                   comment_tite: int = Query(None,
                                           title='Id of the comment',
                                           description='Some description for the comment_title',
                                           alias='commentTitle',
                                           deprecated=True
                                           ),
                                        #    content: str = Body('hi how are you')
                                           content: str = Body(..., min_length= 10, max_length=50,
                                                               regex='^[a-z\s]*$'),
                                        #    content: str = Body(Ellipsis)
                                        v: Optional[List[str]] = Query(['1.0','1.1','1.2']),
                                        comment_id: int = Path(None, gt=5, le=10)
                                           ):
    return {
        'blog':blog,
        'id': id,
        'comment_title':comment_tite,
        'comment_id': comment_id,
        'content': content,
        'version': v
    }

def required_functionality():
    return {'message': 'Learning DaftAPI is important'}