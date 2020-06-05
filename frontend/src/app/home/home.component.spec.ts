import {async, ComponentFixture, TestBed} from '@angular/core/testing';
import {By} from '@angular/platform-browser';
import {DebugElement} from '@angular/core';
import {HomeComponent} from "./home.component";
import {BlogService} from "../service/blog.service";
import { of } from 'rxjs'
import {LoadingComponent} from "../loading/loading.component";
import {PreviewBlogComponent} from "../preview-post/preview-blog.component";

describe('HomeComponent', () => {
  let component: HomeComponent;
  let fixture: ComponentFixture<HomeComponent>;
  let de: DebugElement;
  let blogServiceStub;

  beforeEach(async(() => {
    blogServiceStub = {
      getBlogs: () => of(null),
    };

    TestBed.configureTestingModule({
      declarations: [HomeComponent, LoadingComponent, PreviewBlogComponent],
      providers: [{ provide: BlogService, useValue: blogServiceStub }]
    })
      .compileComponents();  // compile template and css
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HomeComponent);
    component = fixture.componentInstance;
    de = fixture.debugElement;
    fixture.detectChanges();
  });

  it("should create", () => {
    expect(component).toBeTruthy();
  });

  // it("should be boolean", () => {
  //   expect(component.loading).toBeTruthy();
  // });

});
