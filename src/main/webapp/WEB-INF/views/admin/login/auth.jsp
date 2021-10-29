<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
    // 0: 인증 가능 사용자 및 비밀번호 목록.
    String user = "";
    String password = "";
    // 1: form 으로부터 전달된 데이터를 변수에 저장.
    String id = request.getParameter("id");
    String pw = request.getParameter("pw");
    // 2: 사용자 인증
    String redirectUrl = "login?error=login-failed.."; // 인증 실패시 요청 될 url 
    
    if (user.equals(id) && password.equals(pw))
    	redirectUrl = "welcome?id=" + id; // 인증 성공 시 재 요청 url
    
    response.sendRedirect(redirectUrl);
%>