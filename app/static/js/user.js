//tab标签页默认开启控制
$(function(){$('#myTab a').click(function (e) {
    e.preventDefault();
    $(this).tab('show');
    });
})

//在除首页的其他页面对于nav竖导航进行控制
 $(function () {
    $("#navorgan").click(function () {
	
      $("#allnav").toggle();
        if ($("#allnav").is(":hidden")) {
 
            $("#iconcheck").removeClass('icon-chevron-up').addClass('icon-chevron-down');
        } else {
            $("#iconcheck").removeClass('icon-chevron-down').addClass('icon-chevron-up');
        }
    })
 
})

//用户注册控制表单验证
$(function () {
    var ok1 = false;
    var ok2 = false;
    var ok3 = false;
    var ok4 = false;
    var ok5 = false;
    // 验证用户名
    $('input[name="username"]').focus(function () {
    }).blur(function () {
        var username=$(this).val();
        var usernameok=username.replace (/[^\x00-\xff]/g,"rrr").length;;
        if (usernameok>=6 && usernameok <=64) {
            $(this).next().text('');
            ok1 = true;
        } else if(usernameok==0){
            $(this).next().text('用户名不能为空');
        }else{
            $(this).next().text('用户名长度应大于6字节，一个汉字3字节"');
        }
    });
    //验证手机号
    $('input[name="cellphone"]').focus(function () {
    }).blur(function () {
        var isMobile=/^(?:13\d|14\d|15\d|18\d|17\d)\d{5}(\d{3}|\*{3})$/;
        var  phonenum=$(this).val();
        if (isMobile.test(phonenum)) {
            $(this).next().text('');
            ok2 = true;
        } else if(phonenum=="") {
            $(this).next().text('手机号码不能为空');
        }else{
            $(this).next().text('请输入正确的手机号');
        }
 
    });
    //验证密码
    $('input[name="password"]').focus(function () {
        // $(this).next().text('密码应该为6-20位之间');
    }).blur(function () {
        var password=$(this).val();
         var passwordlenth=password.length;
        if (passwordlenth >=6 && passwordlenth <=20) {
            $(this).next().text('');
            ok3 = true;
        } else{
            $(this).next().text('请输入长度为6到20位的密码');
        }
 
    });
 
    //验证确认密码
    $('input[name="password2"]').focus(function () {
    }).blur(function () {
        if ($(this).val() != '' && $(this).val() == $('input[name="password"]').val()) {
            $(this).next().text('');
            ok4 = true;
        } else {
            $(this).next().text('前后密码不一致');
        }
    });
 //验证邮箱
    $('input[name="email"]').focus(function () {
        // $(this).next().text('请输入正确的EMAIL格式');
    }).blur(function () {
        var myreg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
        var email=$(this).val();
        if( myreg.test(email) || email=="")
        {
            $(this).next().text('');
            ok5=true;
        }
        else{
            $(this).next().text('请输入正确格式的邮箱');
        }
 
    });

    //提交按钮,所有验证通过方可提交
    $('#uerregbtn').click(function () {
        alert("da");
        if (ok1 && ok2 && ok3 && ok4 && ok5) {

            $('form').submit();
        } else {
            return false;
        }
    });
 
});
function show(){ 
var box = document.getElementById("boxmore"); 
var text = box.innerHTML; 
var newBox = document.createElement("div"); 
var btn = document.createElement("a");
btn.className="amoremore"; 
newBox.innerHTML = text.substring(0,262); 
btn.innerHTML = text.length > 262 ? "...查看全部" : ""; 
btn.href = "###"; 
btn.onclick = function(){ 
if (btn.innerHTML == "...查看全部"){ 
btn.innerHTML = "收起"; 
newBox.innerHTML = text; 
}else{ 
btn.innerHTML = "...查看全部"; 
newBox.innerHTML = text.substring(0,262); 
} 
} 
box.innerHTML = ""; 
box.appendChild(newBox); 
box.appendChild(btn); 
} 
show();

var degree = ['','很差','差','中','良','优','未评分'];
//重新点评
function addComment2(e,inid,opt,id){
	$.ajax({
		url:'/siteMessage/content',
		type:'post',
		data:'id='+id,
		dataType:'json',
		success:function(data){
			if(data.status==1){
				var list = $('#Addnewskill_119');
				list.eq(0).html(data.talent+'(人才ID：'+data.talentId+')');
				list.eq(1).html(data.job);
				list.eq(2).html(data.ms);
				
				var arr = [data.total,data.expAuth,data.killAuth,data.followTime,data.formality,data.appReact];
				var list2 = $('span.level','#Addnewskill_119');
				$('input[name="InterviewCommentInfoSub[opt]"]').val(opt+1);
				list2.each(function(i,v){
						var a = '';
						
						if(i>0){
							a = 'cjmark';
							$(v).parents('li').find('input').val(arr[i]);
						}
						var str = '';
						if(arr[i]==6){
							for(var n=0;n<=4;n++){
								str += '<i '+a+' class="level_hollow"></i>';
							}
							$(v).parents('li').find('input').prop('disabled',true)
						}else{
							$(v).parents('li').find('input').prop('checked',true)
							for(var n=0;n<arr[i];n++){
								str += '<i '+a+' class="level_solid"></i>';
							}
							for(var n=0;n<(5-arr[i]);n++){
								str += '<i '+a+' class="level_hollow"></i>';
							}
						}
						$(v).html(str);
						$(v).next().html(degree[arr[i]]);
				})
				create_show(119);
			}else{
				ui.error(data.msg,2000);
			}
		}
	})	
}

$(function(){
	//点星星
	$(document).on('mouseover','i[cjmark]',function(){
		var num = $(this).index();
		var pmark = $(this).parents('.revinp');
		var mark = pmark.prevAll('input');

		if(mark.prop('checked')) return false;

		var list = $(this).parent().find('i');
		for(var i=0;i<=num;i++){
			list.eq(i).attr('class','level_solid');
		}
		for(var i=num+1,len=list.length-1;i<=len;i++){
			list.eq(i).attr('class','level_hollow');
		}
		$(this).parent().next().html(degree[num+1]);
        $("#scorenum").val(num+1);

	})
	//点击星星
	$(document).on('click','i[cjmark]',function(){
		var num = $(this).index();
		var pmark = $(this).parents('.revinp');
		var mark = pmark.prevAll('input');

		if(mark.prop('checked')){
			mark.val('');
			mark.prop('checked',false);mark.prop('disabled',true);	
		}else{
			mark.val(num);
            $("#scorenum").val(num+1);
			mark.prop('checked',true);mark.prop('disabled',false);	
		}
	})
	//选框
	$('#Addnewskill_119 input[type="checkbox"]').change(function(){
		if($(this).not(':checked')){//!($(this).prop('checked'))
			$(this).prop('checked',false);$(this).prop('disabled',true)
			var smark = $(this).nextAll('.revinp');
			smark.find('span.revgrade').html('未评分');
			smark.find('i').attr('class','level_hollow');
			smark.val(6);
            $("#scorenum").val(num+1);
		}
	})
	

})
  //alert("");
document.getElementById("Commenttext").focus();
 var chackTextarea = function(obj,num,objTip){
  obj.onkeyup=obj.onfocus=function(){
    if(obj.value.length>=1){
     if (obj.value.length > num) {
       objTip.innerHTML="已超出";
       objTip.style.color="#F00";
       document.getElementById("button").disabled="disabled";
     }else{
        objTip.innerHTML="已输入"+(obj.value.length) +"/"+num+"个字!";
       objTip.style.color="#000";
       document.getElementById("button").disabled="";
     }
    }else{
      document.getElementById("button").disabled="disabled";
    }
  }
 }
 
 chackTextarea(document.getElementById("Commenttext"),500,document.getElementById("commentnum"));
function shake(o){
    var $panel = $("#"+o);
    box_left = ($(window).width() -  $panel.width()) / 2;
    $panel.css({'left': box_left,'position':'absolute'});
    for(var i=1; 4>=i; i++){
        $panel.animate({left:box_left+(40-10*i)-360},10);
        $panel.animate({left:box_left+1.1*(40-10*i)-360},10);
    }
}
//评论时候必须评分
$(function(){
    $("#scorebtn").click(function(){
        var scorenum=$("#scorenum").val();
        if(scorenum==0)
        {
           // alert(scorenum);
            shake('scoreno');
            return false;
        }
    })
})

