//画面ロード時実行関数
window.onload = function(){
  initUnit()
}

//ユニット項目非表示関数
function initUnit(){
  //項目非表示
  document.getElementById("checkUnit1").style.display = "none";
  document.getElementById("checkUnit2").style.display = "none";
}

//グループ項目選択時実行関数
function changeGroup(){
  var elementGroup = document.termsCheck.group
  //μ's選択時
  initUnit()
  if(elementGroup[0].checked){
    document.getElementById("checkUnit1").style.display = "";
  }
  //Aqours選択時
  if(elementGroup[1].checked){
    document.getElementById("checkUnit2").style.display = "";
  }
  //虹選択時
}
//学年項目選択時実行関数
function changeYear(){
  initUnit()
}
