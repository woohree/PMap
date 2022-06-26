import React, { useEffect } from "react"
const { kakao } = window; // 스크립트로  api를 가져오면 window전역 객체에 들어감

const Location=()=>{
	useEffect(()=>{
		const container = document.getElementById('map'); //지도를 담을 DOM
		const options = {
			center: new kakao.maps.LatLng(37.501424752882386, 127.03988746650782), //지도의 중심좌표 center
			level: 3 // level(확대, 축소 정도)
		};
		const map = new kakao.maps.Map(container, options); // 지도 생성 and 객체 return 
		// 마커 생성
		const markerPosition  = new kakao.maps.LatLng(37.501424752882386, 127.03988746650782); 
    const marker = new kakao.maps.Marker({
      position: markerPosition
  	});
  	
		// 마커 위에 커스텀오버레이를 표시
		const content = document.createElement('div');
		content.className = 'overlay';
		content.innerHTML = 'information'

		// 마커를 중심으로 커스텀 오버레이를 표시하기위해 CSS를 이용해 위치를 설정했습니다
		const customOverlay = new kakao.maps.CustomOverlay({
			content: content,
			map: map,
			position: marker.getPosition()       
		});

		// 마커를 클릭했을 때 커스텀 오버레이를 표시
		kakao.maps.event.addListener(marker, 'click', function() {
			customOverlay.setMap(map);
		});

		// 커스텀 오버레이를 닫기
		kakao.maps.event.addListener(map, 'click', function() {
			customOverlay.setMap(null);
		});

		marker.setMap(map);
		customOverlay.setMap(map);
		
		}, []) // useEffect, 2번째 인자 [] 처음 렌더링 될 때 한번만 띄우게함 

		return (
			<div>
				<div id="map" style={{width:"100%", height:"30rem"}}></div> 
			</div>
		)
}
  
  export default Location