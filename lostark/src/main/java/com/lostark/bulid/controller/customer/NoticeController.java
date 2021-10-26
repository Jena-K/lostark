package com.lostark.bulid.controller.customer;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller // �� �������� �����Ұ��̱⶧���� controller
@RequestMapping("/customer/notice/")
public class NoticeController {	//����� �Խ��� ���� ��Ʈ�ѷ�
	/*
	 * �Խ��� ���, ���, ����, ����
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
