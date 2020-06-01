import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import {HttpClientModule} from '@angular/common/http';
import {AppRoutingModule} from './app-routing.module';
import {HomeComponent} from './home/home.component';
import {AboutMeComponent} from './about/about-me.component';
import {ViewBlogComponent} from './view-blog/view-blog.component';
import {NavbarComponent} from './navbar/navbar.component';
import {FooterComponent} from './footer/footer.component';
import {PreviewBlogComponent} from './preview-post/preview-blog.component';
import {AddBlogComponent} from './add-blog/add-blog.component';
import {LoadingComponent} from './loading/loading.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {FormsModule} from '@angular/forms';
import {ApiService} from './service/api.service';
import {MastheadComponent} from './masthead/masthead.component';
import {BlogService} from './service/blog.service';


@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    AboutMeComponent,
    ViewBlogComponent,
    NavbarComponent,
    FooterComponent,
    PreviewBlogComponent,
    AddBlogComponent,
    MastheadComponent,
    LoadingComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    FormsModule,
    AppRoutingModule
  ],
  providers: [ApiService, BlogService],
  bootstrap: [AppComponent]
})
export class AppModule { }
