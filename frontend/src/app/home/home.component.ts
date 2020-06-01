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
  blogs: Blog[];

  constructor(private blogService: BlogService, private router: Router) {}

  ngOnInit() {
    this.getBlogs();
  }

  private getBlogs(): void {
    this.blogService.getBlogs().subscribe(blogs => {
      this.blogs = blogs;
      this.loading = false;
    });
  }

  private refresh(event): void {
    this.blogs = this.blogs.filter(item => item != event);
  }
}
