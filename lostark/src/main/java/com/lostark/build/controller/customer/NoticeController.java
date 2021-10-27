package com.lostark.build.controller.customer;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("customer/notice/")
public class NoticeController { 	// �Խ��� ���� ��Ʈ�ѷ�
	/*
	 *�Խñ� ���, ���, ����, ���� 
	 * list,reg,edit,del
	 * 
	 */
	
	@RequestMapping("list")
	public String list() {
		
		return "customer.notice.list";
	}
	
	@RequestMapping("reg")
	public String reg() {
		
		return "customer.notice.reg";
	}
	
	@RequestMapping("edit")
	public String edit() {
		
		return "customer.notice.edit";
	}
	
	@RequestMapping("del")
	public String del() {
		
		return "customer.notice.del";
	}
}
