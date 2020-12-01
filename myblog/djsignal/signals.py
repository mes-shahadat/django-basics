from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import pre_init, post_init,pre_save,post_save,pre_delete,post_delete, pre_migrate,post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created

# in order to work need to modify apps.py and __init__.py files

@receiver(user_logged_in,sender=User)
def login_successful(sender,request,user, **kwargs):
    # you can use paramiters from this fuction or you can make your own function something like clearing cache
    print('---------------------------------------------------------------------------------')
    print('from user_logged_in signale')
    print('logged in successfully')
    print(f'sender: {sender}')
    print(f'request: {request}')
    print(f'user: {user}')
    print(f'kwargs: {kwargs}')

@receiver(user_logged_out,sender=User)
def log_out(sender,request,user, **kwargs):
    print('---------------------------------------------------------------------------------')
    print('from user_log_out signale')
    print('logged out successfully')
    print(f'sender: {sender}')
    print(f'request: {request}')
    print(f'user: {user}')
    print(f'kwargs: {kwargs}')

@receiver(user_login_failed)
def login_unsuccessful(sender,credentials, request, **kwargs):
    print('---------------------------------------------------------------------------------')
    print('from user_login_unsuccessfull signale')
    print('login was unsuccessfull')
    print(f'sender: {sender}')
    print(f'credentials: {credentials}')
    print(f'request: {request}')
    print(f'kwargs: {kwargs}')

# @receiver(pre_init,sender=User)
# def beginning_init(sender,*args, **kwargs):
#     print('---------------------------------------------------------------------------------')
#     print('from pre init signale')
#     print(f'sender: {sender}')
#     print(f'args: {args}')
#     print(f'kwargs: {kwargs}')

# @receiver(post_init,sender=User)
# def ending_init(sender,*args, **kwargs):
#     print('---------------------------------------------------------------------------------')
#     print('from post init signale')
#     print(f'sender: {sender}')
#     print(f'args: {args}')
#     print(f'kwargs: {kwargs}')

@receiver(pre_save,sender=User)
def beginning_save(sender,instance, **kwargs):
    print('---------------------------------------------------------------------------------')
    print('from pre save signale')
    print('save signal found')
    print(f'sender: {sender}')
    print(f'instance: {instance}')
    print(f'kwargs: {kwargs}')

@receiver(post_save,sender=User)
def ending_save(sender,instance,created, **kwargs):
    if created:
        print('---------------------------------------------------------------------------------')
        print('from post save signale')
        print('new data aded')
        print(f'sender: {sender}')
        print(f'instance: {instance}')
        print(f'created: {created}')
        print(f'kwargs: {kwargs}')
    else:
        print('---------------------------------------------------------------------------------')
        print('from post save signale')
        print('old data updated')
        print(f'sender: {sender}')
        print(f'instance: {instance}')
        print(f'created: {created}')
        print(f'kwargs: {kwargs}')    

@receiver(pre_delete,sender=User)
def beginning_delete(sender,instance, **kwargs):
    print('---------------------------------------------------------------------------------')
    print('from pre delete signale')
    print('data going to be deleted')
    print(f'sender: {sender}')
    print(f'instance: {instance}')
    print(f'kwargs: {kwargs}')

@receiver(post_delete,sender=User)
def ending_delete(sender,instance, **kwargs):
    print('---------------------------------------------------------------------------------')
    print('from post delete signale')
    print('old data deleted')
    print(f'sender: {sender}')
    print(f'instance: {instance}')
    print(f'kwargs: {kwargs}')

@receiver(request_started)
def beginning_request(sender,environ, **kwargs):
    print('---------------------------------------------------------------------------------')
    print('from request started signale')
    print('got request')
    print(f'sender: {sender}')
    print(f'environ: {environ}')
    print(f'kwargs: {kwargs}')

@receiver(request_finished)
def ending_request(sender, **kwargs):
    print('---------------------------------------------------------------------------------')
    print('from request finished signale')
    print('got signal after request finish')
    print(f'sender: {sender}')
    print(f'kwargs: {kwargs}')
    
@receiver(got_request_exception)
def after_exception(sender,request, **kwargs):
    print('---------------------------------------------------------------------------------')
    print('from got request exception signale')
    print('got request exception signal')
    print(f'sender: {sender}')
    print(f'request: {request}')
    print(f'kwargs: {kwargs}')

@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('---------------------------------------------------------------------------------')
    print('from before install app signale')
    print('pre migrate signal')
    print(f'sender: {sender}')
    print(f'app_config: {app_config}')
    print(f'verbosity: {verbosity}')
    print(f'interactive: {interactive}')
    print(f'using: {using}')
    print(f'plan: {plan}')
    print(f'apps: {apps}')
    print(f'kwargs: {kwargs}')

@receiver(post_migrate)
def after_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('---------------------------------------------------------------------------------')
    print('from post install app signale')
    print('post migrate signal')
    print(f'sender: {sender}')
    print(f'app_config: {app_config}')
    print(f'verbosity: {verbosity}')
    print(f'interactive: {interactive}')
    print(f'using: {using}')
    print(f'plan: {plan}')
    print(f'apps: {apps}')
    print(f'kwargs: {kwargs}')

@receiver(connection_created)
def conn_db(sender,connection, **kwargs):
    print('---------------------------------------------------------------------------------')
    print('from connection created signale')
    print('initial connection to database')
    print(f'sender: {sender}')
    print(f'connection: {connection}')
    print(f'kwargs: {kwargs}')