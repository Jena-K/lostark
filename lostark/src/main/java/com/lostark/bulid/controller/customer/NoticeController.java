package com.lostark.bulid.controller.customer;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller // 뷰 페이지를 제공할것이기때문에 controller
@RequestMapping("/customer/notice/")
public class NoticeController {	//사용자 게시판 관련 컨트롤러
	/*
	 * 게시판 목록, 등록, 수정, 삭제
	 * list, reg, edit, del
	 */
	@RequestMapping("list")
	public String list() {
		
		return "/WEB-INF/view/customer/notice/list";
	}
	
	@RequestMapping("reg")
	public String reg() {
		
		return "/WEB-INF/view/customer/notice/reg";
	}
	
	@RequestMapping("edit")
	public String edit() {
		
		return "/WEB-INF/view/customer/notice/edit";
	}
	
	@RequestMapping("del")
	public String del() {
		
		return "/WEB-INF/view/customer/notice/del";
	}
	
}
