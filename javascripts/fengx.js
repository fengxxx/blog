
function fengx(){
	//alert("false")
	input_N.value="曾哥";
	input1.value="123";
	} 
function login(name , key){
	var testUrl="09网游俱乐部.html";
		if (input_N.value =="曾哥"&&input1.value=="123"){
			window.open(testUrl);
		}else{
			window.confirm("密码或用户名错误！")
			
			}
	}
	
function openWind_renren(){
    var testUrl="09网游俱乐部.html";
	window.open(testUrl);

}


function GetLocalIPAddress()
{
    var obj = null;
    var rslt = "";
    try
    {
        obj = new ActiveXObject("rcbdyctl.Setting");
        rslt = obj.GetIPAddress;
        obj = null;
    }
    catch(e)
    {
        //异常发生
    }
    input_Ip.value=rslt
    return rslt;
}