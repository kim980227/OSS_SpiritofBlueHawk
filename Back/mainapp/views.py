from django.shortcuts import render
from .models import Post
from .models import BulletinBoard
from .forms import PostForm
def index(request):

    posts = Post.objects.all()
    # HTML에서 POST방식 request form으로 data받기위한 form 정의(forms.py에서 필드값 정의)
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
    form=PostForm()
    # QuerySet에서 'budget' 키의 밸류를 뽑아서 예산 총합 구하기
    result = 0
    budgetlist = list(Post.objects.values())

    for bl in budgetlist:
        result += bl['budget']
        name = (bl['item'])
        x = bl['spotX']
        y = bl['spotY']
        bud = bl['budget']

    # 3자리 마다 콤마 찍기
    result = format(result, ',')
    bud = format(bud, ',')

    return render(
        request,
        'mainapp/index.html',
        {
            "posts": posts,
            "post_form": form,
            "budget_result": result,
            "budget": bud,
            "name": name,
            "spot_x": x,
            "spot_y": y
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'mainapp/single_post_page.html',
        {
            'post' : post,
        }
    )

def bulletin_board(request):
    bulletins = BulletinBoard.objects.all().order_by('-created_at')
    for bulletin in bulletins:
        bulletin.comments = bulletin.comments.all().order_by('-created_at')
    context = {'bulletins': bulletins}
    return render(request, 'bulletin_board.html', context)

def add_comment(request, bulletin_id):
    bulletin = get_object_or_404(BulletinBoard, pk=bulletin_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.b
