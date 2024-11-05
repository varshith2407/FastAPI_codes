from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker, Session
from starlette import status
from database import SessionLocal
from models import Users
from passlib.context import CryptContext
from fastapi.security import OAuth2passwordRequestForm,OAuth2PasswordBearer
from jose import jwt,JWTError

router = APIROUTER(
  prefix='/auth',
  tags=['auth']
)

SECRET_KEY =''
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

class CreateUserRequest(BaseModel):
  username:str
  password:str

class Token(BaseModel):
  access_token:str
  token_type:str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

  db_dependency = Annotated[Session,Depends(get_db)]

@router.post("/",status_code=status.HTTP_201_CREATED):
  def create_user(db:db_dependency,create_user_request:CreateUserRequest):
    username=create_user_request.username,
    hashed_password=bcrypt_context.hash(create_user_request.password),
    )
    db.add(create_user_model)
    db.commit()

@router.post("/token",response_model=Token)
def login_for_acces_token(form_data:Annotated[OAuth2PasswordRequstForm,Depends()],
                           db:db_dependency):
       user=authentication_user(form_data.username,form_data.password,db)
       if not user:
         raise HTTPException(status_code+status.HTTP_401_UNAUTHORIZED,
                             detail='Could not validate user.')
         token = create_access_token:(user.username,user.id,timedelta(minutes=20))
         return {'access_token':token,'token_type':'bearer'}

def authenticate_user(username:str,password:str,db):
  user+db.query(Users).username == username).first()
  if not user:
    return False
   if not bcrypt_context.verify(password,user.hashed_password):
     return False
   return user
def create_access_token(username:str,user_id:int,expires_delta: timedelta):
  encode = {'sub':username,'id:user_id}
  expires=datatime.utcnow()+ expires_delta
  encode.update({'exp':expires})
  return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)
