
document.addEventListener('DOMContentLoaded', function() {
    var links = document.querySelectorAll('nav li div');
    links.forEach(function(link) {
      link.addEventListener('click', function() {
        links.forEach(function(otherLink) {
          otherLink.classList.remove('active');
        });
        this.classList.add('active');
      });
    });
  });
  function record(){
  window.open('/checklist_main/');
}
  function changeContent(clickedElement) {
  var content = document.getElementById("main");
  var newText;
  switch (clickedElement.innerText) {
    case "음주 정도 확인":
     newText = `
     <header>
            <p id="h1">🍻당신이 얼마나 취했는지 알려줄게요!</p>
            <p id="h2">간단한 정보를 입력하고 음성파일을 업로드해주세요!</p>
        </header>
        <div id="input_info">
            <p>성별 : 
                <select id="sex" style="width: 145px;">
                <option value="man">남성</option>
                <option value="woman">여성</option>
            </select>
            </p>
            <p>나이: 만 <input type="number" style="width: 125px;" id="age"> 세</p>
            <p>체중 : <input id="weight" type="number"> kg</p>
            <p>신장 : <input id="height" type="number"> cm</p>
        </div>
        <button id="enter">입력 완료</button>
        <p style="max-width:fit-content; margin-left:auto; margin-right:auto;">아래 제시문을 또박또박 읽은 음성 파일을 업로드해주세요!</p>
        <div style="max-width:fit-content; margin-left:auto; margin-right:auto;">
            <p>계절이 지나가는 하늘에는</p>
            <p>가을로 가득 차 있습니다.</p>
            <p>나는 아무 걱정도 없이 </p>
            <p>가을 속의 별들을 다 헤일 듯 합니다.</p>
            <p>가슴 속에 하나 둘 새겨지는 별들을</p>
            <p>이제 다 못 헤는 것은 </p>
            <p>쉬이 아침이 오는 까닭이요,</p>
            <p>내일 밤이 오는 까닭이요, </p>
            <p>아직 나의 청춘이 다하지 않은 까닭입니다.</p>
        </div>
        <form action="/upload" method="post" enctype="multipart/form-data">
        <div style="max-width:fit-content; margin-left:auto; margin-right:auto;" id="file_upload">
            <input type="file" name="voiceFile" id="voiceFile" accept="audio/mp4, audio/m4a">
            <input type="submit" value="Upload">
        </div>
    <div style="max-width:fit-content; margin-left:auto; margin-right:auto;">
        <p>제시문 낭독 결과:</p>
        <p>0000000000</p>
    </div>
        </form>
      `;
      break;
    case "음주 캘린더":
      newText = `
      `
      break;
    case "알코올 중독 자가진단":
      newText = `
        <header>
            <p style="font-size: 20px;">✔️음주 체크리스트</p>
        </header>
        <button id="record" onclick='record()'>금일 체크리스트 기록하기</button>
        <div id="history_list"></div>`;
      break;
    case "내 정보":
      newText = ``;
      break;
    default:
      newText = ``;
  }
    content.innerHTML = newText;
    if (clickedElement.innerText === "알코올 중독 자가진단") {
        loadChecklistRecords();
    }
}

function loadChecklistRecords() {
    fetch('/get-records/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const historyList = document.getElementById('history_list');
            if (data.records.length === 0) {
                historyList.innerHTML = '<p>No records found.</p>';
            } else {
                data.records.forEach(record => {
                    const div = document.createElement('div');
                    div.className = 'history';
                    div.innerHTML = `<p>${record.date}</p><img src="static/images/arrow.png" alt="<-">`;
                    div.addEventListener('click', () => {
                        alert(`Total Value: ${record.total_value}`);
                    });
                    historyList.appendChild(div);
                });
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}