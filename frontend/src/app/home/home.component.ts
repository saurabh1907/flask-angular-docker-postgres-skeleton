import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Blog } from '../models/blog';
import {BlogService} from '../service/blog.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: []
})
export class HomeComponent implements OnInit {
  loading: boolean = true;
  addDummyText: string = 'add Dummy';
  blogs: Blog[];

  constructor(private blogService: BlogService) {}

  ngOnInit() {
    this.getBlogs();
  }

  private getBlogs(): void {
    this.blogService.getBlogs().subscribe(blogs => {
      this.blogs = blogs;
      this.loading = false;
    });
  }

  private addDummy(): void {
    if(this.addDummyText == 'add Dummy') {
      console.log("sending dummy");
      this.blogService.addDummy(2).subscribe(res => {
      console.log('Dummy add request sent');
      });
      this.addDummyText = 'Request Sent';
      setInterval(() => this.getBlogs(),10000); //Poll the blogs api every 10 seconds
    }
  }
  private refresh(event): void {
    this.blogs = this.blogs.filter(item => item != event);
  }
}
