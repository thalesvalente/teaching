import { Injectable } from '@nestjs/common';
import { PrismaService } from '../../prisma/prisma.service';
import { Analysis, Prisma } from '@prisma/client';
import { OpenaiService } from '../openai/openai.service';
import { ChatCompletionMessageDto } from '../openai/dto/create-chat-completion.resquest';

@Injectable()
export class AnalysisService {
  getAnalysesByUser(userId: string) {
    throw new Error('Method not implemented.');
  }
  constructor(
    private prisma: PrismaService,
    private openaiService: OpenaiService,
  ) {}

  async createAnalysis(
    scriptId: number,
    initialPrompt: string,
  ): Promise<Analysis> {
    const script = await this.prisma.script.findUnique({
      where: { id: scriptId },
    });

    if (!script) {
      throw new Error('Script not found');
    }

    const messages: ChatCompletionMessageDto[] = [
      { role: 'system', content: 'You are a script analysis assistant.' },
      { role: 'user', content: script.content },
      { role: 'user', content: initialPrompt },
    ];

    const completion = await this.openaiService.createChatCompletion(messages);

    return this.prisma.analysis.create({
      data: {
        scriptId,
        result: completion.choices[0].message.content,
      },
    });
  }

  async getAnalysis(userId: number, scriptId: number): Promise<Analysis[]> {
    return this.prisma.analysis.findMany({
      where: {
        scriptId: scriptId,
        script: {
          userId: userId,
        },
      },
    });
  }

  async findAnalysisById(id: number): Promise<Analysis | null> {
    return this.prisma.analysis.findUnique({ where: { id } });
  }

  async updateAnalysis(
    id: number,
    data: Prisma.AnalysisUpdateInput,
  ): Promise<Analysis> {
    return this.prisma.analysis.update({ where: { id }, data });
  }

  async deleteAnalysis(id: number): Promise<Analysis> {
    return this.prisma.analysis.delete({ where: { id } });
  }
}
