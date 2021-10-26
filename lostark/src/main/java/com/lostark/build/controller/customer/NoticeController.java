package com.lostark.build.controller.customer;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("customer/notice/")
public class NoticeController { 	// 게시판 관련 컨트롤러
	/*
	 *게시글 목록, 등록, 수정, 삭제 
	 * list,reg,edit,del
	 * 
	 */
	
	@RequestMapping("list")
	public String list() {
		
		return "customer/notice/list";
	}
	
	@RequestMapping("reg")
	public String reg() {
		
		return "customer/notice/reg";
	}
	
	@RequestMapping("edit")
	public String edit() {
		
		return "customer/notice/edit";
	}
	
	@RequestMapping("del")
	public String del() {
		
		return "customer/notice/del";
	}
}
